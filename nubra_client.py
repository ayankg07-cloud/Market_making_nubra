from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv

class NubraMarketClient:
    def __init__(self, env="uat"):
        if env.lower()== "uat":
            self.sdk=InitNubraSdk(NubraEnv.UAT)
        else:
            self.sdk=InitNubraSdk(NubraEnv.PROD)
