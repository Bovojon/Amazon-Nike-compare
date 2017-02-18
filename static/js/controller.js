(function() {
  'use strict';

  angular
    .module('compareApp')
    .controller('CompareCtrl', CompareCtrl);


  CompareCtrl.$inject = ['$state', '$http'];
  function CompareCtrl($state, $http) {
    var vm = this;
    vm.submitForm = submitForm;

    vm.formData = {};

    function displayResult() {
       $http
         .get("/static/js/amazon-output.json")
         .then(function(response) {
           console.log("Success");
           vm.results = response;
         });
    };

    function submitForm() {
      vm.keyword= vm.formData.keyword
      $http
        .post('/results', vm.keyword)
        .then(function(response) {
          displayResult();
          $state.go('results');
          vm.results = response;
          console.log(vm.results)
        });
    };



    // function postIt() {
    //   vm.keyword;
    //   $http
    //     .post('/', vm.keyword)
    //     .then(function(response) {
    //       console.log("Success");
    //       console.log(response);
    //     });
    // }



  } // End of controller
})();
