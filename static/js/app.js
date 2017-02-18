(function() {
  'use strict';

  angular.module('compareApp', [
    // Angular modules
    'ui.router',
    'ngAnimate',

    // Custom modules
  ])
  .config(configFunction)


  configFunction.$inject = ['$stateProvider', '$urlRouterProvider'];
  function configFunction($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider

    // $stateProvider.state('home', {
    //   url: '/home',
    //   templateUrl: '/static/partials/home.html',
    //   controller: 'CompareCtrl',
    //   controllerAs: 'vm'
    // });
    // $stateProvider.state('about', {
    //   url: '/about',
    //   templateUrl: '../static/partials/about.html',
    //   controller: 'CompareCtrl',
    //   controllerAs: 'vm'
    // });

    .state('home', {
      url: '/home',
      templateUrl: '/static/partials/home.html',
      controller: 'CompareCtrl',
      controllerAs: 'vm'
      })

      .state('home.keyword', {
        // url: '/keyword',
        templateUrl: '/static/partials/form-keyword.html',
        controller: 'CompareCtrl',
        controllerAs: 'vm'
      })

      .state('home.category', {
        // url: '/category',
        templateUrl: '/static/partials/form-category.html',
        controller: 'CompareCtrl',
        controllerAs: 'vm'
      })

      .state('results', {
        url: '/results',
        templateUrl: '/static/partials/results.html',
        controller: 'CompareCtrl',
        controllerAs: 'vm'
      })

      .state('about', {
        url: '/about',
        templateUrl: '../static/partials/about.html',
        controller: 'CompareCtrl',
        controllerAs: 'vm'
      });



  }
})();
