import 'package:flutter/material.dart';
import 'package:health_moni/providers/auth.dart';
import 'package:health_moni/providers/users/patient.dart';

import 'package:health_moni/widgets/app_drawer.dart';
import 'package:health_moni/widgets/tutelary/tutelary_user.dart';
import 'package:health_moni/widgets/tutelary/tutelary_user_list.dart';
import 'package:provider/provider.dart';

class TutelaryScreen extends StatefulWidget {
  static const routeName = '/tutelary';
  Auth _authProv;

  TutelaryScreen(this._authProv);

  //TutelaryScreen();

  @override
  _TutelaryScreenState createState() => _TutelaryScreenState();
}

class _TutelaryScreenState extends State<TutelaryScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Tutelary"),
      ),
      drawer: AppDrawer(),
      body: SingleChildScrollView(
        child: Column(
          children: [
            SizedBox(height: 5),
            TutelaryUserList(widget._authProv.user),
          ],
        ),
      ),
    );
  }
}
