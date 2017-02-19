(function() {
  'use strict';

  angular.module('compareApp', [
    // Angular modules
    'ui.router',
    'ngAnimate',

  ])
  .config(configFunction)


  configFunction.$inject = ['$stateProvider', '$urlRouterProvider'];
  function configFunction($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider
    .state('home', {
      url: '/',
      templateUrl: '/static/partials/home.html',
      controller: 'CompareCtrl',
      controllerAs: 'vm'
      })

      // .state('home.keyword', {
      //   url: 'keyword',
      //   templateUrl: '/static/partials/form-keyword.html',
      //   controller: 'CompareCtrl',
      //   controllerAs: 'vm'
      // })
      //
      // .state('home.category', {
      //   url: 'compare',
      //   templateUrl: '/static/partials/form-category.html',
      //   controller: 'CompareCtrl',
      //   controllerAs: 'vm'
      // })
      //
      // .state('results', {
      //   url: '/results',
      //   templateUrl: '/static/partials/results.html',
      //   controller: 'CompareCtrl',
      //   controllerAs: 'vm'
      // })

      .state('about', {
        url: '/about',
        templateUrl: '../static/partials/about.html',
        controller: 'CompareCtrl',
        controllerAs: 'vm'
      });



  }
})();
