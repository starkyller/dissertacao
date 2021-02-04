import 'package:flutter/material.dart';
import 'package:health_moni/models/users/models.dart';
import 'package:health_moni/providers/auth.dart';
import 'package:provider/provider.dart';

import 'package:health_moni/models/monitoring_solutions/models.dart';
import 'package:health_moni/providers/monitoring_solutions/solution.dart';
import 'package:health_moni/providers/users/patient.dart';
import 'package:health_moni/providers/monitoring_solutions/monitoring_category.dart';

import 'package:health_moni/widgets/app_drawer.dart';

class HomeScreen extends StatefulWidget {
  static const routeName = '/home';
  Auth _authProv;
  HomeScreen(this._authProv);

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  var _isInit = true;
  var _isPatient = true;

  @override
  void initState() {
    // no init state o provider so funcina com o listen:false, mas como nao
    // queremos isso aqui temos de arranajr outra solucao
    // Provider.of<MonitoringCategories>(context, listen: false).loadItems();

    // Provider.of<Solutions>(context, listen: false)
    //     .getItem("cd9f8981-1005-4e7c-8a2e-eb38278829f0");
    // Provider.of<Patients>(context, listen: false).loadItem();

    // podia se usar esta hack mas é melhor evitar hacks
    // Future.delayed(Duration.zero).then((_) {
    //   Provider.of<MonitoringCategories>(context).loadItems();
    // });124ea599-01a2-49a1-be2f-c1fcb04d003e

    super.initState();
  }

  @override
  void didChangeDependencies() {
    if (_isInit) {
      if (widget._authProv.user.userType == UserTypes.PATIENT) {
        Provider.of<Patients>(context, listen: false).loadItem();
      } else {
        _isPatient = false;
      }

      _isInit = false;
    }

    super.didChangeDependencies();
  }

  void _teste123() {
    var a = 11;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Dashboard"),
      ),
      drawer: AppDrawer(),
      // body: Center(
      //   child: Text('Home Page'),
      // ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Text('teste123'),
            FlatButton(
              color: Theme.of(context).accentColor,
              onPressed: _teste123,
              child: Text("ee"),
            ),
          ],
        ),
      ),
    );
  }
}

// class HomeScreen extends StatelessWidget {
//   static const routeName = '/home';

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text("Home"),
//       ),
//       drawer: AppDrawer(),
//       body: Center(
//         child: Text('Home Page'),
//       ),
//     );
//   }
// }
