import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';

import 'package:http/http.dart' as http;

import 'package:shared_preferences/shared_preferences.dart';

import 'package:health_moni/exceptions/http_exception.dart';
import 'package:health_moni/app-config.dart' show apiDomain;

enum UserTypes { PATIENT, MEDICALSTAFF }

class Auth with ChangeNotifier {
  String _token;
  String _userAlias;
  UserTypes _userType;

  String _baseURL = apiDomain + "auth/";

  Map<String, String> _headers = {
    'Content-Type': 'application/json; charset=UTF-8',
  };

  bool get isAuth {
    return token != null;
  }

  String get token {
    if (_token != null) return _token;

    return null;
  }

  String get userAlias {
    return _userAlias;
  }

  UserTypes get userType {
    return _userType;
  }

  Map<String, String> get headers {
    return _headers;
  }

  Future<void> login(String username, String password) async {
    final url = _baseURL + "login/";

    Map<String, dynamic> userInfo = {
      "username": username,
      "password": password,
    };

    try {
      final response = await http.post(
        url,
        headers: _headers,
        body: json.encode(userInfo),
      );

      final responseData = json.decode(response.body);

      // wrong credentials
      if (responseData.containsKey('non_field_errors'))
        throw HttpException(responseData['non_field_errors'].toString());

      if (response.statusCode >= 400)
        throw HttpException(responseData.toString());

      _token = responseData['token'];
      _userAlias = responseData['alias'];

      if (responseData['type'] == "PATIENT") {
        _userType = UserTypes.PATIENT;
      } else {
        _userType = UserTypes.MEDICALSTAFF;
      }

      _headers.putIfAbsent('Authorization', () => "Token $_token");

      notifyListeners();

      final prefs = await SharedPreferences.getInstance();
      final userData = json.encode({
        'token': _token,
        'userAlias': _userAlias,
        'userTypeIndex': _userType.index,
      });
      prefs.setString('auth_data', userData);
    } catch (e) {
      throw e;
    }
  }

  Future<bool> tryAutoLogin() async {
    final prefs = await SharedPreferences.getInstance();

    if (!prefs.containsKey('auth_data')) return false;

    final userAuthData =
        json.decode(prefs.get('auth_data')) as Map<String, Object>;

    _token = userAuthData['token'];
    _userAlias = userAuthData['userAlias'];
    _userType = UserTypes.values[userAuthData['userTypeIndex']];

    _headers.putIfAbsent('Authorization', () => "Token $_token");

    notifyListeners();

    return true;
  }

  void logout() async {
    final url = _baseURL + "logout/";

    try {
      final response = await http.post(
        url,
        headers: _headers,
      );

      if (response.statusCode >= 400) {
        final responseData = json.decode(response.body);
        throw HttpException(responseData.toString());
      }
    } catch (e) {
      throw e;
    }

    _headers.remove("Authorization");
    _token = null;
    _userAlias = null;
    _userType = null;

    notifyListeners();

    final prefs = await SharedPreferences.getInstance();
    prefs.remove('auth_data');
  }
}
