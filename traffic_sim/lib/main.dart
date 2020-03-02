import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Map(),
    );
  }
}

class Map extends StatefulWidget {
  @override
  _MapState createState() => _MapState();
}

class _MapState extends State<Map> {
  String getFreq(List objects) {
    // var Things = {};
    var countCars = 0, countPersons = 0;
    // print(objects);
    objects.forEach((object) {
      var st = object.toString().split(':');
      var key = st[0];
      if (key == "car") {
        countCars = countCars + 1;
      } else if (key == "person") {
        countPersons = countPersons + 1;
      }
      // Things[key] = st[1];
    });
    // Things.forEach((key, value) {
    // print(countCars);
    // });
    return 'Cars : $countCars\nPersons : $countPersons';
  }

  TextEditingController controller = new TextEditingController();
  String timer;

  @override
  Widget build(BuildContext context) {
    final mediaQuery = MediaQuery.of(context);
    return Scaffold(
      resizeToAvoidBottomInset: false,
      appBar: AppBar(
        title: Text('DashBoard'),
      ),
      body: Column(
        children: <Widget>[
          SizedBox(height: 30,),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
              RaisedButton(
                color: Colors.red,
                child: Text(
                  "Red",
                  style: TextStyle(color: Colors.white, fontSize: 16),
                ),
                onPressed: () {
                  Firestore.instance
                      .collection('interrupt')
                      .document('status')
                      .setData({'status': 'Red'});
                },
              ),
              RaisedButton(
                color: Colors.green,
                child: Text(
                  "Green",
                  style: TextStyle(color: Colors.white, fontSize: 16),
                ),
                onPressed: () {
                  Firestore.instance
                      .collection('interrupt')
                      .document('status')
                      .setData({'status': 'Green'});
                },
              ),
            ],
          ),
          SizedBox(height: 10,),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
              Text(
                'Timer duration: ',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Container(
                decoration: BoxDecoration(
                    border: Border.all(
                  color: Colors.black,
                  width: 3,
                )),
                width: 100,
                height: 30,
                child: TextField(
                  controller: controller,
                  keyboardType: TextInputType.number,
                  onChanged: (text) {
                    timer = text;
                  },
                  // onSubmitted: (text) {
                  //   Firestore.instance
                  //       .collection('timer')
                  //       .document('counttime)
                  //       .setData({'time': text});
                  // },
                ),
              ),
              RaisedButton(
                onPressed: () {
                  Firestore.instance
                      .collection('timer')
                      .document('counttime')
                      .setData({'time': timer});
                  controller.clear();
                },
                color: Colors.blue,
                child: Text(
                  'Submit',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 16,
                  ),
                ),
              ),
            ],
          ),
          SizedBox(height: 20,),
          Container(
            height: mediaQuery.size.height * 0.5,
            width: double.infinity,
            decoration: BoxDecoration(
              border: Border.all(
                color: Colors.black,
                width: 3,
              ),
            ),
            child: Center(
              child: StreamBuilder<QuerySnapshot>(
                  stream: Firestore.instance.collection('person').snapshots(),
                  builder: (BuildContext context,
                      AsyncSnapshot<QuerySnapshot> snapshot) {
                    if (snapshot.hasError)
                      return new Text('Error: ${snapshot.error}');
                    switch (snapshot.connectionState) {
                      case ConnectionState.waiting:
                        return new Text('Loading...');
                      default:
                        return new ListView(
                          children: snapshot.data.documents
                              .map((DocumentSnapshot document) {
                            return new ListTile(
                              // title: new Text(document['object_list'].map((i) => i.toString()).join("\n")),
                              title: new Text(getFreq(document['object_list'])),
                            );
                          }).toList(),
                        );
                    }
                  }),
            ),
          ),
          Container(
            padding: EdgeInsets.all(20),
            // height: mediaQuery.size.height * 0.5,
            width: double.infinity,
            child: Text(
              'Log',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
              textAlign: TextAlign.center,
            ),
          ),
        ],
      ),
    );
  }
}
