# XL Releae CliQr plugin

[![Build Status][xlr-cliqr-plugin-travis-image]][xlr-cliqr-plugin-travis-url]
[![License: MIT][xlr-cliqr-plugin-license-image]][xlr-cliqr-plugin-license-url]
![Github All Releases][xlr-cliqr-plugin-downloads-image]

[xlr-cliqr-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-cliqr-plugin.svg?branch=master
[xlr-cliqr-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-cliqr-plugin
[xlr-cliqr-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-cliqr-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-cliqr-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-cliqr-plugin/total.svg

## Preface

This document describes the functionality provided by the XL Release CliQr plugin.

See the [XL Release reference manual](https://docs.xebialabs.com/xl-release) for background information on XL Release and release automation concepts.

## Overview

This is a plugin to be developed via CliQr REST API.  A simple ListUsers method is included as an example.  See the complete API documentation [here](http://docs.cliqr.com/display/API/API+Overview).

## Requirements

* XL Release 4.5+

## Installation

* Place the JAR file (found on the Release tab above) in the `SERVER_HOME/plugins` directory. 

* Restart the XL Release server.

## Usage

* Define a CliQr server under Shared Configuration.
* Add the List Users task to your release template.

