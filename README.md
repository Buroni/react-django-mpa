# react-django-mpa

Uses a simple `Message` data model with `messages` app, which displays messages in a list or detail view at routes `messages/` and `messages/<pk>` respectively. 

## Setup
In the repo root directory, install dependencies:
```
npm i --dev
pip install -r requirements.txt
```

Run the Django project:
```
python manage.py runserver
```

Run the webpack bundler:
```
npm run watch
```

## How Pages are Served

* `messages/static/js/components`: Stores the React components needed to be compiled and used by the app.
* `messages/static/js/pages`: Each page of the app is stored here in its own file. Each page uses `ReactDOM.render` to render a component in `components/` as the root component of the page, and pass `window.props` (originally data from Django) into the component. These page files can be loaded inside a HTML template after being bundled. Each page has its own React root, unlike an SPA which has one root branching into the whole application.
* `webpack.config.js`: The `entry` export in this file contains the entry points for all the pages in the application. The entry points in this example are the files inside `pages/`

So in order to create a new page in the app, first the React component for that page is put inside `components/ReactComponentName.js`. Then the React render code is placed in `pages/reactComponentName.js` and the page file is added as an entry point in `webpack.config.js`.

## Interface between Django and Webpack/React

* Each Django view which is to pass data into a displayed React component should use the `ReactMixin`. This mixin attaches the props to be passed into the react component onto the `context` object, alongside the name of the webpack bundle to be loaded and some page metadata. 
* The `ReactMixin` uses the `base.html` template, which loads the bundle using `django-webpack-loader` based on the `page_name` specified by the view component. In this template, the react props provided by the view's context are also attached to `window.props`, ready to be injected into the component by `pages/componentName` as mentioned in the previous section.

## Todo
* Add Typescript and SCSS support.
* Figure out how our mobx data model will work inside a MPA.


## Reading

The webpack installation process was taken from this article, and modified to work with the latest Babel:
https://medium.com/uva-mobile-devhub/set-up-react-in-your-django-project-with-webpack-4fe1f8455396

The `ReactMixin` logic was partly taken from
https://github.com/mikaelengstrom/django-react-polls-example/

