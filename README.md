# Taipei Bus Tracker Service

A Flask-based application designed to track all buses in Taipei City. The application integrates with the TDX Transport Data Exchange Service Platform's API to fetch real-time bus data.

## Prerequisites

Before running the application, there are several steps you need to take:

1. Register for a dedicated API key at the [TDX Transport Data Exchange Service Platform](https://tdx.transportdata.tw/). Additionally, register for the Gmail email sending service to obtain the necessary credentials.
2. Fill in your private credentials in the `app.env.dev` file. Once done, rename `app.env.dev` to `app.env`. The `app.env` file should contain:
    - `BUS_APP_ID`: Your API ID from the TDX platform
    - `BUS_APP_KEY`: Your API Key from the TDX platform
    - `MAIL_USERNAME`: Your registered Gmail username
    - `MAIL_PASSWORD`: Your Gmail password
3. Run the application using the following command:`docker-compose up --build`


## Features

1. **Real-time Bus Information**: Send a request to `127.0.0.1/bus/<bus_number>` to receive real-time bus information. This includes the bus number, direction, and estimated arrival times for each stop. For a sample payload, refer to `bus_simulation.json`.
2. **Email Notification Subscription**: Send a request to `127.0.0.1/subscribe/<email>/<bus_number>/<direction>/<station>` to subscribe to notifications for a specific bus stop. You'll receive an email notification 3 minutes before the bus arrives at your subscribed stop. To see an example of a user's subscription payload, refer to `user_simulation.json`.

## In Development

1. **Email Sending Simulation**: Due to recent changes in Gmail's policies, the email sending functionality is currently in a simulation state. It's not entirely suitable for app scenario, so alternate solutions are being developed.

## Feedback and Contributions

Your feedback is valuable to help improve this application. If you encounter any issues or have suggestions, please create an issue on this repository. Contributions are also welcome!
