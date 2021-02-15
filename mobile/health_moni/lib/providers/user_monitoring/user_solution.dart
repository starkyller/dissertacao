import 'dart:io';
import 'dart:convert';

import 'package:health_moni/providers/auth.dart';
import 'package:health_moni/providers/monitoring_solutions/solution.dart';
import 'package:http/http.dart' as http;

import 'package:flutter/foundation.dart';

import 'package:health_moni/models/monitoring_solutions/models.dart'
    show Solution;

import 'package:health_moni/app-config.dart' show apiDomain;

class UserMonitoring with ChangeNotifier {
  Auth _auth;
  Solutions _solutionProv;
  String _baseURL = apiDomain + "us/";

  List<Solution> _subscribedSolutions = [];

  UserMonitoring(this._auth, this._solutionProv);

  List<Solution> get items {
    return [..._subscribedSolutions];
  }

  Future<void> loadItems() async {
    final url = _baseURL + "user-solutions/${_auth.user.alias}/";
    List<Solution> loadedSubscribedSolutions = [];

    try {
      final response = await http.get(url, headers: _auth.headers);

      if (response.statusCode == 404) throw HttpException("Not Found");

      if (response.statusCode >= 400)
        throw HttpException("Error code ${response.statusCode.toString()}");

      final extractedData = json.decode(response.body) as List<dynamic>;

      if (extractedData == null) return;

      await Future.wait(extractedData.map((orderData) async {
        final slugy = orderData["solution"]["slug"];
        await _solutionProv.getItem(slugy).then((value) {
          loadedSubscribedSolutions.add(value);
        });
      }));

      _subscribedSolutions = loadedSubscribedSolutions;

      notifyListeners();
    } catch (e) {
      throw e;
    }
  }

  //
}
