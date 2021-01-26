// 10.0.2.2 is the localhost of the physical machine where
// the android vm is running
//const _apiDomain = "http://10.0.2.2:8000/api/";
const _apiDomain = "http://192.168.1.13:8000/api/";

Map<String, String> _headers = {
  'Content-Type': 'application/json; charset=UTF-8',
};

String get apiDomain {
  return _apiDomain;
}

Map<String, String> get headers {
  return _headers;
}
