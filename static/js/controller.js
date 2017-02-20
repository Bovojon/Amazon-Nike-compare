(function() {
  'use strict';

  angular
    .module('compareApp')
    .controller('CompareCtrl', CompareCtrl);


  CompareCtrl.$inject = ['$state', '$http', '$timeout'];
  function CompareCtrl($state, $http, $timeout) {
    var vm = this;
    vm.submitForm = submitForm;
    vm.formData = {};

    vm.website = false;
    vm.activated = false;

    console.log(vm.keyword);

    function submitForm(keyword) {
      vm.activated = true;
      console.log(keyword);
      $http
        .post('/', vm.keyword)
        .then(function(response) {
          console.log(response);
          vm.results = response.data;
        })
        .then(function(response) {
          $http
            .get("/static/js/amazon-output.json")
            .then(function(response) {
              vm.data = response.data;
              vm.items = vm.data.items;
              console.log(typeof response);
              console.log(typeof vm.items);
              vm.activated = false;
              vm.website = true;
            });


          $http
            .get("/static/js/nike-output.json")
            .then(function(response) {
              vm.datan = response.data;
              vm.itemsn = vm.datan.items;
              console.log(typeof response);
              console.log(typeof vm.itemsn);
            });
        });
    };

  } // End of controller
})();
