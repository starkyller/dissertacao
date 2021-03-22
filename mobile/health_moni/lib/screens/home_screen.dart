import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'package:provider/provider.dart';

import 'package:health_moni/models/users/models.dart';
import 'package:health_moni/providers/auth.dart';
import 'package:health_moni/providers/user_monitoring/user_solution.dart';
import 'package:health_moni/providers/users/patient.dart';
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
  var _isLoading = false;
  var _isPatient = true;

  Future<void> startServiceInPlatform(UserMonitoring _provi) async {
    if (Platform.isAndroid) {
      var methodChannel = MethodChannel("com.example.health_moni.messages");

      String data = await methodChannel.invokeMethod("startService");
      debugPrint(data);

      Map<String, dynamic> args = {};

      args["headers"] = widget._authProv.headers;
      args["baseUrl"] = _provi.baseUrl + "data-collection/";
      args["subscriptions"] = _provi.itemsInJson;
      // widget._authProv.headers;
      data = await methodChannel.invokeMethod("loadSubscriptions", args);
      debugPrint(data);
    }
  }

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

  Future<void> _loadPatientData() async {
    await Provider.of<Patients>(context, listen: false).loadItem();
    UserMonitoring _userMonprov =
        Provider.of<UserMonitoring>(context, listen: false);

    await _userMonprov.loadItems();

    await startServiceInPlatform(_userMonprov);
  }

  void _loadMedicalStaffData() {}

  @override
  void didChangeDependencies() {
    if (_isInit) {
      if (widget._authProv.user.userType == UserTypes.PATIENT) {
        setState(() {
          _isLoading = true;
        });

        _loadPatientData();
        setState(() {
          _isLoading = false;
        });
        //Provider.of<Patients>(context, listen: false).loadItem();
      } else {
        _isPatient = false;
        _loadMedicalStaffData();
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
      body: _isLoading
          ? Center(
              child: CircularProgressIndicator(),
            )
          : SingleChildScrollView(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    //crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Text(
                        'You can minimize the app now,\n it will continue to run in the background',
                      ),
                      // FlatButton(
                      //   color: Theme.of(context).accentColor,
                      //   onPressed: _teste123,
                      //   child: Text("ee"),
                      // ),
                    ],
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
