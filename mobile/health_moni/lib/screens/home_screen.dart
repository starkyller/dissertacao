import 'package:flutter/material.dart';
import 'package:health_moni/models/monitoring_solutions/models.dart';
import 'package:health_moni/providers/monitoring_solutions/solution.dart';

import 'package:health_moni/widgets/app_drawer.dart';
import 'package:provider/provider.dart';

import 'package:health_moni/providers/monitoring_solutions/monitoring_category.dart';

class HomeScreen extends StatefulWidget {
  static const routeName = '/home';

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  var _isInit = true;

  @override
  void initState() {
    // no init state o provider so funcina com o listen:false, mas como nao
    // queremos isso aqui temos de arranajr outra solucao
    // Provider.of<MonitoringCategories>(context, listen: false).loadItems();

    Provider.of<Solutions>(context, listen: false)
        .getItem("cd9f8981-1005-4e7c-8a2e-eb38278829f0");

    // podia se usar esta hack mas é melhor evitar hacks
    // Future.delayed(Duration.zero).then((_) {
    //   Provider.of<MonitoringCategories>(context).loadItems();
    // });124ea599-01a2-49a1-be2f-c1fcb04d003e

    super.initState();
  }

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
