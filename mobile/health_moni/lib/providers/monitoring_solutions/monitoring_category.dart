import 'dart:io';
import 'dart:convert';

import 'package:http/http.dart' as http;

import 'package:flutter/foundation.dart';

import 'package:health_moni/models/monitoring_solutions/models.dart'
    show MonitoringCategory;

import 'package:health_moni/app-config.dart' show apiDomain;

class MonitoringCategories with ChangeNotifier {
  Map<String, String> _headers;

  MonitoringCategories(this._headers);

  List<MonitoringCategory> _items = [];

  String _baseURL = apiDomain + "ms/";

  List<MonitoringCategory> get items {
    return [..._items];
  }

  Future<MonitoringCategory> getItem(String uuid) async {
    final url = _baseURL + "monitoring-category/$uuid/";

    try {
      final response = await http.get(url, headers: _headers);

      if (response.statusCode == 404) throw HttpException("Not Found");

      if (response.statusCode >= 400)
        throw HttpException("Error code ${response.statusCode.toString()}");

      final extractedData = json.decode(response.body);

      MonitoringCategory obj = MonitoringCategory.fromJson(extractedData);

      return obj;
    } catch (e) {
      throw e;
    }
  }

  Future<void> loadItems() async {
    final url = _baseURL + "monitoring-category/";
    List<MonitoringCategory> loadedMonintoringCategories = [];

    try {
      final response = await http.get(url, headers: _headers);

      if (response.statusCode == 404) throw HttpException("Not Found");

      if (response.statusCode >= 400)
        throw HttpException("Error code ${response.statusCode.toString()}");

      final extractedData = json.decode(response.body) as List<dynamic>;

      if (extractedData == null) return;

      extractedData.forEach((orderData) {
        loadedMonintoringCategories.add(MonitoringCategory.fromJson(orderData));
      });

      _items = loadedMonintoringCategories;

      notifyListeners();
    } catch (e) {
      throw e;
    }
  }

  //
}
