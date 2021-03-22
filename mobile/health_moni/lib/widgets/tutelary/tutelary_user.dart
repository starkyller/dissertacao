import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

// import '../models/transaction.dart';

class TutelaryUserListItem extends StatelessWidget {
  // const TransactionItem({
  //   Key key,
  //   @required this.transaction,
  //   @required this.deleteTx,
  // }) : super(key: key);

  // final Transaction transaction;
  // final Function deleteTx;
  final String username;

  TutelaryUserListItem(this.username);

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 5,
      margin: EdgeInsets.symmetric(
        vertical: 4,
        horizontal: 5,
      ),
      child: ListTile(
        leading: CircleAvatar(
          radius: 30,
          child: Padding(
            padding: const EdgeInsets.all(6),
            child: FittedBox(
              child: Icon(Icons.perm_identity),
            ),
          ),
        ),
        title: Text(
          this.username,
        ),
        // subtitle: Text(
        //   DateFormat.yMMMMd().format(transaction.date),
        // ),
      ),
    );
  }
}
