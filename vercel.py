{
    "version": 2,
    "builds": [
        {
            "src": "backend/app.py",
            "use": "@vercel/python",
            "config": {
                "maxLambdaSize": "15mb",
                "runtime": "python3.10"
            }
        },
        {
            "src": "build.sh",
            "use": "@vercel/static-build",
            "config": {
                "distDir": "staticfiles_build"
            }
        }
    ],
    "routes": [
        {
            "src": "/static/(.*)",
            "dest": "/static/$1"
        },
        {
            "src": "/(.*)",
            "dest": "backend/app.py"
        }
    ]

}
