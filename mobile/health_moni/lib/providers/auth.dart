import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';

import 'package:http/http.dart' as http;

import 'package:shared_preferences/shared_preferences.dart';

import 'package:health_moni/models/users/models.dart';
import 'package:health_moni/exceptions/http_exception.dart';
import 'package:health_moni/app-config.dart' show apiDomain;

enum UserTypes { PATIENT, MEDICALSTAFF }

class Auth with ChangeNotifier {
  User _user;

  String _baseURL = apiDomain + "auth/";

  Map<String, String> _headers = {
    'Content-Type': 'application/json; charset=UTF-8',
  };

  bool get isAuth {
    return _user != null;
  }

  User get user {
    return _user;
  }

  Map<String, String> get headers {
    return _headers;
  }

  Future<void> login(String username, String password) async {
    final url = _baseURL + "login/";

    Map<String, dynamic> userInfo = {
      "username": username,
      "password": password
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

      _user = User.fromJson(responseData);
      _user.username = username;

      _headers.putIfAbsent('Authorization', () => "Token ${_user.token}");

      notifyListeners();

      final prefs = await SharedPreferences.getInstance();

      final userData = json.encode(_user);
      prefs.setString('user', userData);
    } catch (e) {
      throw e;
    }
  }

  Future<bool> tryAutoLogin() async {
    final prefs = await SharedPreferences.getInstance();

    if (!prefs.containsKey('user')) return false;

    final userJson = json.decode(prefs.get('user')) as Map<String, Object>;
    _user = User.fromJson(userJson);

    _headers.putIfAbsent('Authorization', () => "Token ${_user.token}");

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
    _user = null;

    notifyListeners();

    final prefs = await SharedPreferences.getInstance();
    prefs.remove('user');
  }

  //
}
