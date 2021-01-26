import 'package:flutter/material.dart';
import 'package:health_moni/models/monitoring_solutions/models.dart';
import 'package:health_moni/providers/monitoring_solutions/solution.dart';

import 'package:health_moni/widgets/app_drawer.dart';
import 'package:provider/provider.dart';

import 'package:health_moni/providers/monitoring_solutions/monitoring_category.dart';

class SplashScreen extends StatelessWidget {
  static const routeName = '/splash';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // appBar: AppBar(
      //   title: Text("Home"),
      // ),
      // drawer: AppDrawer(),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            SizedBox(
              child: CircularProgressIndicator(
                  // strokeWidth: 4.0,
                  // valueColor : AlwaysStoppedAnimation(Colors.white),
                  ),
              height: 200.0,
              width: 200.0,
            ),
          ],
        ),
      ),
    );
  }
}
