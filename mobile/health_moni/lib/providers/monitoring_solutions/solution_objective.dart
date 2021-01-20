import 'dart:io';
import 'dart:convert';

import 'package:http/http.dart' as http;

import 'package:flutter/foundation.dart';

import 'package:health_moni/models/monitoring_solutions/models.dart'
    show SolutionObjective;

import 'package:health_moni/app-config.dart' show apiDomain;

class SolutionObjectives with ChangeNotifier {
  Map<String, String> _headers;

  SolutionObjectives(this._headers);

  List<SolutionObjective> _items = [];

  String _baseURL = apiDomain + "ms/";

  List<SolutionObjective> get items {
    return [..._items];
  }

  Future<SolutionObjective> getItem(String uuid) async {
    final url = _baseURL + "solution-objective/$uuid/";

    try {
      final response = await http.get(url, headers: _headers);

      if (response.statusCode == 404) throw HttpException("Not Found");

      if (response.statusCode >= 400)
        throw HttpException("Error code ${response.statusCode.toString()}");

      final extractedData = json.decode(response.body);

      SolutionObjective obj = SolutionObjective.fromJson(extractedData);

      return obj;
    } catch (e) {
      throw e;
    }
  }

  Future<void> loadItems() async {
    final url = _baseURL + "solution-objective/";
    List<SolutionObjective> loadedSolutionObjectives = [];

    try {
      final response = await http.get(url, headers: _headers);

      if (response.statusCode == 404) throw HttpException("Not Found");

      if (response.statusCode >= 400)
        throw HttpException("Error code ${response.statusCode.toString()}");

      final extractedData = json.decode(response.body) as List<dynamic>;

      if (extractedData == null) return;

      extractedData.forEach((orderData) {
        loadedSolutionObjectives.add(SolutionObjective.fromJson(orderData));
      });

      _items = loadedSolutionObjectives;

      notifyListeners();
    } catch (e) {
      throw e;
    }
  }

  //
}
