(function() {
  'use strict';

  angular
    .module('compareApp')
    .controller('CompareCtrl', CompareCtrl);


  CompareCtrl.$inject = ['$state', '$http'];
  function CompareCtrl($state, $http) {
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
        });
    };

    function displayData() {
      $http
        .get("/static/js/amazon-output.json")
        .then(function(response) {
          vm.data = response.data;
        });
    }





  } // End of controller
})();
