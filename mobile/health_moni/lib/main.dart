import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:health_moni/models/monitoring_solutions/models.dart';
import 'package:health_moni/providers/monitoring_solutions/solution.dart';
import 'package:health_moni/providers/user_monitoring/user_solution.dart';
import 'package:health_moni/providers/users/patient.dart';
import 'package:health_moni/screens/splash_screen.dart';
import 'package:health_moni/screens/tutelary/tutelary_home_screen.dart';
import 'package:provider/provider.dart';

import 'package:health_moni/providers/monitoring_solutions/monitoring_category.dart';
import 'package:health_moni/providers/monitoring_solutions/solution_objective.dart';

import 'package:health_moni/providers/auth.dart';

import 'package:health_moni/screens/auth_screen.dart';
import 'package:health_moni/screens/home_screen.dart';

void main() {
  // permitir apenas orientacao vertical
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations(
    [
      DeviceOrientation.portraitUp,
      DeviceOrientation.portraitDown,
    ],
  );
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    // só as widgets que estiverem subscritas ao provider é que são
    // reconstruidas com a alteração de dados
    // sempre que se instancia um objeto de uma classe como estamos a fazer
    // aqui é melhor usar a abordagem com o create para eficiencia e reduzer
    // probabilidades de bugs, por outro lado se for para reutilizar um objeto
    // é melhor a abordagem presente no products_grid.dart
    // o multiProvider permite inserir multiplos prividers de uma vez
    var _providersList = [
      ChangeNotifierProvider(
        create: (ctx) => Auth(),
      ),
      ChangeNotifierProxyProvider<Auth, Patients>(
        create: (ctx) => Patients(
          null,
        ),
        update: (ctx, auth, previousOrdersObject) => Patients(
          auth,
        ),
      ),
      ChangeNotifierProxyProvider<Auth, MonitoringCategories>(
        create: (ctx) => MonitoringCategories(
          null,
        ),
        update: (ctx, auth, previousOrdersObject) => MonitoringCategories(
          auth.headers,
        ),
      ),
      ChangeNotifierProxyProvider<Auth, SolutionObjectives>(
        create: (ctx) => SolutionObjectives(
          null,
        ),
        update: (ctx, auth, previousOrdersObject) => SolutionObjectives(
          auth.headers,
        ),
      ),
      ChangeNotifierProxyProvider3<Auth, SolutionObjectives,
          MonitoringCategories, Solutions>(
        create: (ctx) => Solutions(
          null,
          null,
          null,
        ),
        update: (ctx, auth, soliObjs, moniCats, previousOrdersObject) =>
            Solutions(
          auth.headers,
          soliObjs,
          moniCats,
        ),
      ),
      ChangeNotifierProxyProvider2<Auth, Solutions, UserMonitoring>(
        create: (ctx) => UserMonitoring(
          null,
          null,
        ),
        update: (ctx, auth, sols, previousOrdersObject) => UserMonitoring(
          auth,
          sols,
        ),
      ),
    ];

    return MultiProvider(
      providers: _providersList,
      child: Consumer<Auth>(
        builder: (ctx, auth, _) => MaterialApp(
          title: 'Health Moni',
          theme: ThemeData(
            primarySwatch: Colors.teal,
            accentColor: Colors.greenAccent,
          ),
          home: auth.isAuth
              ? HomeScreen(auth)
              : FutureBuilder(
                  future: auth.tryAutoLogin(),
                  builder: (ctx, authResultSnapshot) =>
                      authResultSnapshot.connectionState ==
                              ConnectionState.waiting
                          ? SplashScreen()
                          : AuthScreen(),
                ),
          routes: {
            SplashScreen.routeName: (ctx) => SplashScreen(),
            TutelaryScreen.routeName: (ctx) => TutelaryScreen(auth),
          },
        ),
      ),
    );
  }

  //
}
