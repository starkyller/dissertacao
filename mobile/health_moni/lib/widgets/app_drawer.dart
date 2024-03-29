import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'package:health_moni/providers/auth.dart';

class AppDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Column(
        children: [
          AppBar(
            title: Text("Navigation"),
            // desabilita aquele botao de retroceder com a setinha
            automaticallyImplyLeading: false,
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.home),
            title: Text("Home"),
            onTap: () {
              Navigator.of(context).pushReplacementNamed('/');
            },
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.shield),
            title: Text("My tutelary"),
            onTap: () {
              Navigator.of(context).pushReplacementNamed('/tutelary');
            },
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.exit_to_app),
            title: Text("Log out"),
            onTap: () {
              Provider.of<Auth>(context, listen: false).logout();
              Navigator.of(context).pop();
              Navigator.of(context).pushReplacementNamed('/auth');
            },
          ),
        ],
      ),
    );
  }
}
