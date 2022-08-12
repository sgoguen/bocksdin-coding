### Intro
Welcome back! Last time we implemented Swagger 
to give us a UI for making calls to our API and 
to see what information the routes may be expecting.
However, this was purely for documentation purposes
and won't prevent unexpected or bad data from being
sent to the routes.

That's where J O I comes in. Joi is an npm package 
that provides a readable and modular way to validate
input before it can cause problems. We'll be adding Joi
to our API to make it more secure, and I encourage you
to check out the documentation at "joi.dev/api" for more details.

### Installation
The first thing we need to do is install the Joi npm package.
Let's open our terminal, and run `npm i joi`. This will install
the latest version of the package.

### Schema
Joi allows us to create schema against which data is tested.
Using various data identifiers and rules, we can make sure only
data we expect or need is making it through. So what we need to do now
is define our validation schema.

Let's start by creating a new folder called `validation` and create a new file called `validation.js` in it.

If you'll recall, we have four routes; a get, post, put, and delete. The get route doesn't expect any information, so we can forgoe that one and we can start with the post schema. The post route is expecting a body with an `entries` array that holds objects with keys `title` and `due_date`.