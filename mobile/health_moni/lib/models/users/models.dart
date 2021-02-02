import 'package:flutter/foundation.dart';

enum UserTypes { PATIENT, MEDICALSTAFF }

class User {
  final String alias;
  final String token;
  final UserTypes userType;
  String username;

  User({
    @required this.alias,
    this.token,
    this.userType,
    this.username,
  });

  factory User.fromJson(dynamic json) {
    final _userType =
        json['type'] == "PATIENT" ? UserTypes.PATIENT : UserTypes.MEDICALSTAFF;

    return User(
      alias: json['alias'],
      username: json['username'] ?? "",
      token: json['token'],
      userType: _userType,
    );
  }

  factory User.fromJsonAliasOnly(dynamic json) {
    return User(
      alias: json['alias'],
    );
  }

  Map<String, dynamic> toJson() => {
        'alias': this.alias,
        'username': this.username,
        'token': this.token,
        'type': this.userType == UserTypes.PATIENT ? "PATIENT" : "MEDICALSTAFF",
      };

  //
}

class Patient extends User {
  List<User> guardians;
  List<User> guardianOf;

  Patient({
    @required username,
    @required alias,
    @required token,
    this.guardians,
    this.guardianOf,
  }) : super(
          username: username,
          alias: alias,
          token: token,
          userType: UserTypes.PATIENT,
        );

  factory Patient.fromUser({User user}) {
    return Patient(
      alias: user.alias,
      username: user.username,
      token: user.token,
    );
  }

  factory Patient.fromJson(dynamic json) {
    final guardiansJsonList = json['guardians'];
    final guardianOfJsonList = json['guardian_of'];

    List<User> _guardians =
        List<User>.from(guardiansJsonList.map((model) => User.fromJson(model)));

    List<User> _guardianOf = List<User>.from(
        guardianOfJsonList.map((model) => User.fromJson(model)));

    return Patient(
      username: json['username'],
      alias: json['alias'],
      token: json['token'],
      guardians: _guardians,
      guardianOf: _guardianOf,
    );
  }

  //
}
