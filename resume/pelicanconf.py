#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'leschtz'
SITENAME = 'resume'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = 'en'
THEME = '/Users/leschtz/git/resume'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Personal Data
NAME = 'Lukas Schuetz'
TAGLINE = 'Junior Software Engineer' + '\n' + 'CS Student'
PIC = 'profile.png'

#sidebar links
EMAIL = 'schuetz.lukas@sbg.at'
# PHONE = '+43 (0) 660 55 97 96 3'
WEBSITE = 'leschtz.me'
LINKEDIN = 'leschtz'
GITHUB = 'leschtz'
# TWITTER = 'N/A'

CAREER_SUMMARY = "I'm a CS student @TUGraz and a Junior Software Engineer @ams AG"

SKILLS = [
	{
		'title': 'Python',
   		'level': '85'
   	},
  	{
  		'title': 'C/C++',
   		'level': '70'
   	},
    {
  		'title': 'Bash',
  		'level': '70'
  	}
]

SOFT_SKILLS = ['communicative', 'team-oriented', 'well-structured', 'reliable', 'self-confident', 'autonomous']

PROJECT_INTRO = 'This is a small collection of my projects, not directly related to work or my studies.'
PROJECTS = [
	{
		'title': 'senf',
		'tagline': 'is a script collection, to handle a "student environment", this is currently a work in progress, but makes some essential work on the command line easier for me.'
	}
]

LANGUAGES = [
	{
		'name': 'German',
		'description': 'Native'
	},
	{
		'name': 'English',
		'description': 'Professional'
	},
	{
		'name': 'Spanish',
		'description': 'Basic'
	}
]

INTERESTS = [
	'Running',
	'Cycling',
	'Nature'
]

EXPERIENCES = [
	{
		'job_title': 'Junior Software Engineer',
		'time': 'February 2018 - present, Part-Time | Full-Time',
		'company': 'ams AG',
		'description': 'Analysing and Supporting Design Verification Workflow. Implementing Verification Tasks in System Verilog. Implementing a script collection, to enhance automatic DV Methodology. Meeting Owner for agile development.',
		'details': [
			'Supporting Design Verification',
			'Analysing Design Verification Workflow for Automation',
			'Creating Standardized, Company-Wide Templates and Workflows',
			'Meeting Owner for Agile Development'
		]
	},
	{
		'job_title': 'Junior Software Engineer, Internship',
		'time': 'July 2017 - September 2017, Full-Time',
		'company': 'ams AG',
		'description': 'Implementing a Requirements Workflow into IC Development. The idea was to re-use Requirements Engineered data for automatable tasks.',
		'details': [
			'Requirements Management',
			'Evaluating and Analysing ReqIF Standard',
			'Development of Eclipse Plugins, to export ReqIF data to XML, CSV, JSON',
			'Internal Project Support for Requirements Management'
		]
	}, 
	{
		'job_title': 'Associated Member of Technical Staff, Internship',
		'time': 'July 2016 - September 2016, Full-Time',
		'company': 'Maxim Integrated',
		'description': 'Implementing a SW GUI for Keyless-Go Receiver LF IC SD306. Implementing an embedded firmware test system, based on UML data. Maintaining an equipment database with MS Access',
		'details': [
			'Embedded Firmware Test System | UML, OCL, Python',
			'SW GUI for Keyless-Go Receiver LF IC SD306 | Python, C++',
			'Maintain Equipment Database | MS Access'
		]
	}
]

EDUCATIONS = [
	{
		'degree': 'Bachelor of Science, Computer Science',
		'meta': 'Technical University of Graz',
		'time': '2015 - present'
	},
	{
		'degree': 'Bundesrealgymnasium Hallein',
		'meta': 'Hallein, Salzburg, Austria',
		'time': '2012 - 2015'
	}
]

