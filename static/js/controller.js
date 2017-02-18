(function() {
  'use strict';

  angular
    .module('compareApp')
    .controller('CompareCtrl', CompareCtrl);


  CompareCtrl.$inject = ['$state', '$http'];
  function CompareCtrl($state, $http) {
    var vm = this;

    function makeCall() {
      vm.shoe= "roshe one";

       $http
         .get("static/js/data.json")
         .then(function(response) {
           vm.elems = response;
           console.log("Success");
           console.log(response);
         });
    };

    function postIt() {
      vm.keyword;
      $http
        .post('/', vm.keyword)
        .then(function(response) {
          console.log("Success");
          console.log(response);
        });
    }


  } // End of controller
})();
