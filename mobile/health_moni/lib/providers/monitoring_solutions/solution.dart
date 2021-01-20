import 'dart:io';
import 'dart:convert';

import 'package:http/http.dart' as http;

import 'package:flutter/foundation.dart';

import 'package:health_moni/models/monitoring_solutions/models.dart'
    show Solution;

import 'package:health_moni/providers/monitoring_solutions/monitoring_category.dart';
import 'package:health_moni/providers/monitoring_solutions/solution_objective.dart';

import 'package:health_moni/app-config.dart' show apiDomain;

class Solutions with ChangeNotifier {
  Map<String, String> _headers;
  SolutionObjectives _solutionObjectivesProv;
  MonitoringCategories _monitoringCategoriesProv;

  Solutions(
    this._headers,
    this._solutionObjectivesProv,
    this._monitoringCategoriesProv,
  );

  List<Solution> _items = [];

  String _baseURL = apiDomain + "ms/";

  List<Solution> get items {
    return [..._items];
  }

  Future<Solution> getItem(String uuid) async {
    final url = _baseURL + "solution/$uuid/";

    try {
      final response = await http.get(url, headers: _headers);

      if (response.statusCode == 404) throw HttpException("Not Found");

      if (response.statusCode >= 400)
        throw HttpException("Error code ${response.statusCode.toString()}");

      final extractedData = json.decode(response.body);

      final objective =
          await _solutionObjectivesProv.getItem(extractedData["objective"]);

      final category =
          await _monitoringCategoriesProv.getItem(extractedData["category"]);

      Solution obj = Solution.fromJson(extractedData, objective, category);

      return obj;
    } catch (e) {
      throw e;
    }
  }

  // Future<void> loadItems() async {
  //   final url = _baseURL + "solution-objective/";
  //   List<Solution> loadedSolutionObjectives = [];

  //   try {
  //     final response = await http.get(url, headers: _headers);

  //     if (response.statusCode == 404) throw HttpException("Not Found");

  //     if (response.statusCode >= 400)
  //       throw HttpException("Error code ${response.statusCode.toString()}");

  //     final extractedData = json.decode(response.body) as List<dynamic>;

  //     if (extractedData == null) return;

  //     extractedData.forEach((orderData) {
  //       loadedSolutionObjectives.add(Solution.fromJson(orderData));
  //     });

  //     _items = loadedSolutionObjectives;

  //     notifyListeners();
  //   } catch (e) {
  //     throw e;
  //   }
  // }

  //
}
