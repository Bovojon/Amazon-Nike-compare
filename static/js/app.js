(function() {
  'use strict';

  angular.module('compareApp', [
    // Angular modules
    'ui.router',

    // Custom modules
  ])
  .config(configFunction)


  configFunction.$inject = ['$stateProvider', '$urlRouterProvider'];
  function configFunction($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/home');

    $stateProvider.state('home', {
      url: '/home',
      templateUrl: '/static/partials/home.html',
      controller: 'CompareCtrl',
      controllerAs: 'vm'
    });
    $stateProvider.state('about', {
      url: '/about',
      templateUrl: '../static/partials/about.html',
      controller: 'CompareCtrl',
      controllerAs: 'vm'
    });
  }


})();
