import 'package:flutter/material.dart';

import 'package:health_moni/widgets/app_drawer.dart';

class HomeScreen extends StatelessWidget {
  static const routeName = '/home';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Home"),
      ),
      drawer: AppDrawer(),
      body: Center(
        child: Text('Home Page'),
      ),
    );
  }
}
