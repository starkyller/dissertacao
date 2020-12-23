import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'package:health_moni/providers/auth.dart';

import 'package:health_moni/screens/auth_screen.dart';
import 'package:health_moni/screens/home_screen.dart';

void main() {
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
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (ctx) => Auth(),
        )
      ],
      child: Consumer<Auth>(
        builder: (ctx, auth, _) => MaterialApp(
          title: 'Health Moni',
          theme: ThemeData(
            primarySwatch: Colors.purple,
            accentColor: Colors.deepOrange,
          ),
          home: auth.isAuth
              ? HomeScreen()
              : FutureBuilder(
                  future: auth.tryAutoLogin(),
                  builder: (ctx, authResultSnapshot) =>
                      authResultSnapshot.connectionState ==
                              ConnectionState.waiting
                          ? HomeScreen()
                          : AuthScreen(),
                ),
          // home: AuthScreen(),
          routes: {
            // ProductDetailScreen.routeName: (ctx) => ProductDetailScreen(),
            // CartScreen.routeName: (ctx) => CartScreen(),
            // OrdersScreen.routeName: (ctx) => OrdersScreen(),
            // UserProductsScreen.routeName: (ctx) => UserProductsScreen(),
            // EditProductScreen.routeName: (ctx) => EditProductScreen(),
          },
        ),
      ),
    );
  }
}
