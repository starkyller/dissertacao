import 'package:flutter/foundation.dart';
import 'package:uuid/uuid.dart';

class Slugable {
  final String slug;

  Slugable({
    @required this.slug,
  });

  factory Slugable.fromJson(dynamic json) {
    return Slugable(
      slug: json['slug'],
    );
  }
}

class MonitoringCategory extends Slugable {
  String designation;

  MonitoringCategory({
    @required slug,
    this.designation = "",
  }) : super(
          slug: slug,
        );

  factory MonitoringCategory.fromJson(dynamic json) {
    return MonitoringCategory(
        slug: json['slug'], designation: json['designation']);
  }
}

class SolutionObjective extends Slugable {
  String designation;

  SolutionObjective({
    @required slug,
    this.designation = "",
  }) : super(
          slug: slug,
        );

  factory SolutionObjective.fromJson(dynamic json) {
    return SolutionObjective(
      slug: json['slug'],
      designation: json['designation'],
    );
  }
}

class Solution extends Slugable {
  final String name;
  final String description;
  final MonitoringCategory category;
  final SolutionObjective objective;
  final Map<String, dynamic> jsonSchema;

  Solution({
    @required slug,
    @required this.name,
    @required this.description,
    @required this.category,
    @required this.objective,
    @required this.jsonSchema,
  }) : super(
          slug: slug,
        );

  factory Solution.fromJson(
    dynamic json,
    SolutionObjective solObj,
    MonitoringCategory monCat,
  ) {
    return Solution(
      slug: json['slug'],
      name: json['name'],
      description: json['description'],
      category: monCat,
      objective: solObj,
      jsonSchema: json['sampleJsonSchema'],
    );
  }
}
