'use strict';

var angular = require('angular');


module.exports = angular.module("myModule", [])
    .controller('myController1', require('./controller1.js'))
    .controller('myController2', require('./controller2.js'))