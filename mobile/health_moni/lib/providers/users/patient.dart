import 'dart:io';
import 'dart:convert';

import 'package:http/http.dart' as http;

import 'package:flutter/foundation.dart';

import 'package:health_moni/app-config.dart' show apiDomain;
import 'package:health_moni/models/users/models.dart';
import 'package:health_moni/providers/auth.dart';

class Patients with ChangeNotifier {
  Auth _auth;

  Patients(this._auth);

  Patient get user {
    return _auth.user;
  }

  String _baseURL = apiDomain + "auth/";

  Future<Patient> loadItem() async {
    final url = _baseURL + "user-info/${_auth.user.alias}/";

    try {
      final response = await http.get(url, headers: _auth.headers);

      if (response.statusCode == 404) throw HttpException("Not Found");

      if (response.statusCode >= 400)
        throw HttpException("Error code ${response.statusCode.toString()}");

      final extractedData = json.decode(response.body);
      final guardiansJsonList = extractedData['guardians'];
      final guardianOfJsonList = extractedData['guardian_of'];

      List<User> _guardians = List<User>.from(
          guardiansJsonList.map((model) => User.fromJsonAliasOnly(model)));

      List<User> _guardianOf = List<User>.from(
          guardianOfJsonList.map((model) => User.fromJsonAliasOnly(model)));

      final _patient = Patient.fromUser(user: _auth.user);
      _patient.guardians = _guardians;
      _patient.guardianOf = _guardianOf;

      _auth.patientUser = _patient;
      notifyListeners();

      return _patient;
    } catch (e) {
      throw e;
    }
  }

  //
}
