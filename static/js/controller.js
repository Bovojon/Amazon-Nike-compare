(function() {
  'use strict';

  angular
    .module('compareApp')
    .controller('CompareCtrl', CompareCtrl);


  CompareCtrl.$inject = ['$state', '$http', '$timeout'];
  function CompareCtrl($state, $http, $timeout) {
    var vm = this;
    vm.submitForm = submitForm;
    vm.displayData = displayData;
    vm.formData = {};

    function submitForm() {
      vm.keyword= vm.formData.keyword
      $http
        .post('/results', vm.keyword)
        .then(function(response) {
          console.log(response);
          vm.results = response.data;
        })
        .then(function(response) {
          $timeout(displayData(),5000);
        });
    };

    function displayData() {
      $http
        .get("/static/js/amazon-output.json")
        .then(function(response) {
          vm.data = response.data;
          vm.items = vm.data.items;
          console.log(typeof response);
          console.log(typeof vm.items);
          console.log(vm.items);
        });

      vm.results = JSON.stringify(vm.items);
      console.log(typeof vm.results);
    }





  } // End of controller
})();
