from settings import Settings

api = {
    "saas": {
        "local":"http://saaspro.com",
        "dev":"http://sctest-saaspro.cheoo.com",
        # "dev":"http://localhost:9201",
    },
    "haidaoNew":{
        "local":"http://localhost:9003/new",
        "dev":"http://sctest-haidao.cheoo.com/new"
    },
}

setting = Settings({})
setting.set('env', 'DEV')
setting.set('api',api)
setting.set('version','v4.9')
