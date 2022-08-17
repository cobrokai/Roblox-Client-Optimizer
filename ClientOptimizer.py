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
    input("Press the Enter key to exit...")
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
        input("Press the Enter key to exit...")
        exit()
else:
    print(f"ClientSettings directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press the Enter key to exit...")
    exit()

# Write to ClientAppSettings.json
if found:
    try:
        with open(found, 'w') as ClientAppSettings:
            data = {"DFFlagDebugRenderTC2ForceSingleTextureSet":"true","DFFlagDebugRenderTC2ForceSingleMip":"true","DFFlagUseSort":"true","FFlagUseSortForClient":"true","DFFlagUseRoundRobin":"true","FFlagUseRoundRobinForClient":"true","DFFlagReplicatorCheckReadTableCollisions":"true","DFFlagReplicatorReadPSWithout":"true","DFFlagReplicateProtectedStringForScript":"true","DFFlagOnlyNetworkHumanoidStatePropertyReplication":"true","DFFlagNetworkHumanoidStatePropertyReplication3":"true","DFFlagNetworkHumanoidStatePropertyReplicationWarmup":"true","DFFlagNoCompletenessForNeverReplicateParent":"true","FFlagHSRClusterImprovement":"true","FFlagImprovedLQMaterialDetiled":"true","FFlagLCQualityCheckUVMismatch":"true","FFlagLCQualityCheck":"true","DFFlagFmodCalculateDeviceLatency":"true","FFlagFixLCCompressOnDifferentClothesOrder":"true","DFFlagAdjustMixedPriorityFairlyAdditiveAsymptote":"true","FFlagFastClusterVertexDeclOpts":"true","FFlagEnableFastClustercompletenessCheckWatcher":"true","FFlagHttpRetryOn424":"true","FFlagHttpRetryOn564":"true","FFlagHttpServiceNeverCache":"false","FFlagHttpRetryOnTimeout":"true","DFFlagRenderTC2Async":"false","FFlagRenderTC2_Disable":"true","FFlagRenderSkipMediumpShaderLoad":"true","FFlagRenderSkipTerrainHQShaderLoad":"true","FFlagRenderSkipTerrainSuperHQShaderLoad":"true","FFlagGraphicsGLEnableHQShadersExclusion":"true","FFlagGraphicsGLEnableSuperHQShadersExclusion":"true","FFlagGraphicsVulkanEnableHQShadersExclusion":"true","FFlagGraphicsVulkanEnableSuperHQShadersExclusion":"true","FFlagGraphicsSkipHQShaders":"true","FFlagGraphicsSkipSuperHQShaders":"true","FFlagSimSolverCacheForces":"true","FFlagSimSolverCacheForces2":"true","FFlagRenderTextureManagerMemoryPrioritizationOrphaned":"true","FFlagSimUseDeterministicAssemblyArray":"true","FFlagPredictedOOMExitContinueChoice":"false","FFlagWriteBootstrapperMetrics":"false","FFlagEnableCheckingOnDisabledChannels":"false","DFFlagRenderTC2_EnableTexCoordPacking2":"true","DFFlagRenderTC2_DiscardGeometryData2":"true","FFlagRemoveRedundantFontPreloading":"true","DFFlagTerrain_UnpackOnDemand_FastSave3":"true","FFlagTerrain_UnpackOnDemand3":"true","FFlagTerrain_UnpackOnDemand_Network":"true","FFlagEnableGameSignalRWithWindows1":"true","DFFlagRefactorReceiveQueue":"true","FFlagAnimatorAndADFRefactorInternal":"true","FFlagTaskSchedulerEnableOptimizedDomainPopping":"true","DFFlagCreateAnimationThrottlingInertializer":"true","DFFlagAnimationThrottlingInertialization":"true","DFFlagStreamingSolverReportMissingSet":"true","DFFlagStreamingInstanceQuotaWhenNoTerrainFix":"true","DFFlagStreamJobAvoidEuclideanDistance":"true","FFlagRenderTC2LOD2":"true","FFlagAdornRenderDrawPolygonsAsUi":"true","FFlagFixUIRTFlip":"true","FFlagGuiHidingApiSupport":"true","FFlagImageLabelRenderUIStrokeWithTransparentBackground":"true","FFlagIncrementalPatchBuilderRefactor3":"true","DFFlagEnableVisibilityService":"true","FFlagEnableCaptureMode":"true","FFlagFixGraphicsQuality":"true","FFlagCommitToGraphicsQualityFix":"true","DFIntCrashUploadToBacktracePercentage":"0","FFlagFixTextureCompositorFramebufferManagement2":"true","FFlagInitializeBeforeAuthentication2":"true","FFlagFlushDeferQueueOnInput":"true","FFlagFlushDeferQueueOnRunState":"true","DFFlagDataModelFasterTaskProcessing":"true","FFlagGenericTexturesMaintainAspectRatio":"true","DFFlagHttpNetworkType":"true","FFlagMemoryPrioritizationEnabledForTextures":"true","FFlagFailedTexturePackShowColor":"true","FFlagTextureReductionViaGenericReload":"true","FFlagTextureRestorationViaGenericReload":"true","DFFlagThrottleDeveloperConsoleEvents":"true","FFlagAppealToBootstrapperOnStartup":"false","DFFlagUseRoundRobin":"true","FFlagUseRoundRobinForClient":"true","DFFlagUseSort":"true","FFlagUseSortForClient":"true","FFlagLeaveStartingCoreScriptsToPlaceLauncher":"true","FFlagFinishFetchingAssetsCorrectly":"true","FFlagTerrainWaitForAssets":"true","FFlagHandleAltEnterFullscreenManually":"false","FFlagExecDynInitTests":"false","FFlagEnableQuickGameLaunch":"true","FFlagEnableLoadingScreenPlaceIconTween":"true","DFFlagTweenServiceOnStepped":"true","FFlagLoadTheLoadingScreenFaster":"true","FFlagLoadTheLoadingScreenEvenFaster":"true","FFlagCoreScriptFasterCreate":"true","FFlagCoreScriptSyncMultiInstance2":"true","DFFlagEnableFlushAfterPurge":"true","FFlagCharacterTaskQueueReschedule":"true","FFlagAsyncFontLoading2":"true","FFlagPreloadAllFonts":"true","FFlagPreloadTextureItemsOption4":"true","FFlagPreloadMinimalFonts":"true","FFlagJoinTime_AllowFullTexturePrioUpdate":"true","DFFlagUseConstantBufferViews":"true","FFlagBatchAssetApi":"true","DFFlagHttpClientOptimizeReqQueuing":"true","FFlagRigidBodyLazyUpdating":"false","FFlagHumanoidDeferredSyncFunction5":"true","FFlagHumanoidParallelUseManager4":"true","FFlagHumanoidParallelOnStep":"true","FFlagHumanoidParallelOnStep2":"true","FFlagHumanoidParallelFixTickleFloor":"true","FFlagHumanoidParallelFixTickleFloor2":"true","FFlagHumanoidParallelFasterSetCollision":"true","FFlagHumanoidParallelFasterWakeUp":"true","FFlagHumanoidParallelSafeCofmUpdate":"true","FFlagHumanoidParallelSafeUnseat":"true","FFlagEngineTruncationEnabledForIngameSettingsV2":"true","FFlagCloudsUseBC4Compression":"true","FFlagDualStreamVertexData5":"true","FFlagWindowsUseHardwareCursor":"true","FFlagEngineHardwareCursorSupport":"true","FIntClientCompressionFormatRequestPC":"3","FFlagBetterTrackpadScrolling":"true","FFlagOptimizeNumUpdateEntityCalls7":"true","FFlagGfxWindowAverage":"true","FFlagRenderFastConvolutionOutdoor":"true","FFlagReduceGuiStateGfxGuiInvalidation":"true","FFlagLightCullNoPreRotation":"true","FFlagFastGPULightCulling":"true","FFlagFastGPULightCulling2":"true","FFlagFastGPULightCulling3":"true","FFlagFastGPULightCulling4":"true","FFlagFastGPULightCulling5":"true","FFlagRenderCacheLocalLightCameras":"true","FFlagRenderTC2_FixBakeCacheContent":"true","FFlagDontCreatePingJob":"true","DFFlagQueueDataPingFromSendData":"true","FFlagAnimationClipMemCacheEnabled":"true","FFlagRenderGetLastLODErrorFix":"true","FFlagRenderAlternativeShadowLod":"true","DFFlagUseSIMDCulling":"true","DFFlagExtentsUseSIMDFunctions":"true","FFlagVoxelizerMeshPerExtentsScale":"true","FFlagOptimizeSkeletonGetBoneIndexByPart":"true","FFlagOptimizeFCMeshGeneratorReplaceParentIndices":"true","FFlagOptimizeFCMeshGeneratorTransformSource":"true","DFFlagAnimatorLodOptOutPhase":"true","DFFlagRenderCompositorExperimentEnabled":"true","DFIntRenderCompositorExperimentPercent":"10000","FFlagRenderHalfresShadowsGlsles":"true","FFlagRenderShadowUseLastLOD":"true","FFlagBatchGfxGui2":"true","FFlagBillboardGuiDistanceStepping2":"true","DFFlagReduceTrussSearchDistance2":"true","FFlagHttpMinUseGzip":"true","DFFlagPlayerConfigurer2866":"true","FFlagPlayerConfigurer2759":"true","DFFlagPlayerConfigurerRunLMSTest":"true","FIntLmsClientRollout2":"10000","DFFlagSimOptimizeInterpolationReturnPreviousIfSmallMovement2":"true","DFFlagSimIfNoInterp2":"true","FFlagForceFSMCPULightCulling":"true","FFlagThrottleLightGridUpdate3":"true"}
            json.dump(data, ClientAppSettings)
            print("Optimization flags applied successfully")
    except FileNotFoundError:
        print("ClientAppSettings.json not found. Please retry.")
        print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
        input("Press the Enter key to exit...")
        exit()
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press the Enter key to exit...")
    exit()
else:
    print(f"ClientSettings directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press the Enter key to exit...")
    exit()