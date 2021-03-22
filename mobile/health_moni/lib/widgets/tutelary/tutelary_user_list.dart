import 'package:flutter/material.dart';
import 'package:health_moni/models/users/models.dart';
import 'package:health_moni/widgets/tutelary/tutelary_user.dart';

class TutelaryUserList extends StatelessWidget {
  // final List<User> guardiansOf;
  final Patient patient;

  TutelaryUserList(this.patient);

  @override
  Widget build(BuildContext context) {
    return patient.guardianOf.isEmpty
        ? LayoutBuilder(builder: (ctx, constraints) {
            return Column(
              children: <Widget>[
                Text(
                  'You are not guardian of anyone!',
                  style: Theme.of(context).textTheme.headline6,
                ),
              ],
            );
          })
        : ListView.builder(
            shrinkWrap: true,
            itemCount: patient.guardianOf.length,
            itemBuilder: (ctx, index) {
              return TutelaryUserListItem(
                patient.guardianOf[index].alias,
              );
            },
          );
  }
}
