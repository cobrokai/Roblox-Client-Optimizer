# Credits to the original script: https://github.com/KEA12/RobloxFullScreenOptimizer
# Edited by nul#3174 to actually be more useful

# Import Libraries
import os
import time
import json

# Define Variables
path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions"
found = ""
start = time.time()

# Find Roblox Game Directory
for file in os.listdir(path):
    if file.startswith("version-"):
        for exe in os.listdir(f"{path}\\{file}"):
            if "RobloxPlayerBeta.exe" in exe:
                found = f"{path}\\{file}"
                print(f"Found Roblox Game directory: {found}")
                break

# Create ClientSettings Folder
if found:
    try:
        os.makedirs(f"{found}\\ClientSettings")
        found = f"{found}\\ClientSettings"
        print("Created ClientSettings Folder")
    except FileExistsError:
        print("ClientSettings folder already exists")
        found = f"{found}\\ClientSettings"
else:
    print(f"Roblox Game directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()


# Create ClientAppSettings.json
if found:
    if not os.path.exists(f"{found}\\ClientAppSettings.json"):
        os.path.join(found, "ClientAppSettings.json")
        found = f"{found}\\ClientAppSettings.json"
        print("ClientAppSettings.json created successfully")
    else:
        print("ClientAppSettings.json already exists")
        print(f"Client optimization is already enabled.")
        print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
        input("Press any key to exit...")
        exit()
else:
    print(f"ClientSettings directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()

# Write to ClientAppSettings.json
if found:
    try:
        with open(found, 'w') as ClientAppSettings:
            data = {"FFlagHandleAltEnterFullscreenManually": "false", "FFlagEnableQuickGameLaunch": "true", "FFlagEnableLoadingScreenPlaceIconTween": "true", "DFFlagTweenServiceOnStepped": "true", "FFlagLoadTheLoadingScreenFaster": "true", "FFlagLoadTheLoadingScreenEvenFaster": "true", "FFlagCoreScriptFasterCreate": "true", "FFlagCoreScriptSyncMultiInstance2": "true", "DFFlagEnableFlushAfterPurge": "true", "FFlagCharacterTaskQueueReschedule": "true", "FFlagAsyncFontLoading2": "true", "FFlagPreloadAllFonts": "true", "FFlagPreloadTextureItemsOption4": "true", "FFlagPreloadMinimalFonts": "true", "FFlagJoinTime_AllowFullTexturePrioUpdate": "true", "DFFlagUseConstantBufferViews": "true", "FFlagBatchAssetApi": "true", "DFFlagHttpClientOptimizeReqQueuing": "true", "FFlagRigidBodyLazyUpdating": "true", "FFlagHumanoidDeferredSyncFunction5": "true", "FFlagHumanoidParallelUseManager4": "true", "FFlagHumanoidParallelFasterSetCollision": "true", "FFlagHumanoidParallelFasterWakeUp": "true", "FFlagHumanoidParallelSafeCofmUpdate": "true", "FFlagHumanoidParallelSafeUnseat": "true"}
            json.dump(data, ClientAppSettings)
            print("Optimization flags applied successfully")
    except FileNotFoundError:
        print("ClientAppSettings.json not found. Please retry.")
        print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
        input("Press any key to exit...")
        exit()
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()
else:
    print(f"ClientSettings directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()
