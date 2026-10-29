# ResourceNodeMarker — Satisfactory 1.2 port

Development fork of [ASCsk/ResourceNodeMarker](https://github.com/ASCsk/ResourceNodeMarker).
Automatically discovers nearby resource nodes and groups them into colored map markers.
Original authorship and existing content are preserved.

**Status: Development Editor build and Windows Shipping package succeed. In-game behavior is not yet verified.**

## Target

- Satisfactory 1.2; local target CL 513885.
- Satisfactory Mod Loader 3.12 source at commit `8eebc9e659f0b2ff4392d2f8cf6e2cff60c8ea49`,
  with game headers updated to CL 513885.
- Custom Satisfactory Unreal Engine 5.6.1, not stock Epic Unreal Engine.
- Wwise 2025.1.6.9117 with Unreal integration 2025.1.6.9117.4248.
- Windows game target. Dedicated-server and multiplayer compatibility are not established.

The plugin's minimum game version follows the SML 3.12 SDK baseline. It is a dependency
constraint, not a claim that every later game build has been tested.

## Changes so far

- Use full resource-header paths required by current build settings.
- Call the current `GetResourcePurityText` API.
- Convert stored UObject references to `TObjectPtr` and expose the containing node/cluster
  arrays to garbage collection.
- Target SML 3.12 and prepare the plugin for Game Features with initial state `Active`.

## Set up and build

Follow the modding team's [dependency setup](https://docs.ficsit.app/satisfactory-modding/latest/Development/BeginnersGuide/dependencies.html)
and [project setup](https://docs.ficsit.app/satisfactory-modding/latest/Development/BeginnersGuide/project_setup.html).

1. Install Visual Studio 2022 C++ desktop/game workloads and the exact SDK/toolset
   specified in the dependency guide, including MSVC v143 14.38.
2. Link GitHub to Epic Games, accept the organization invitation, and complete
   [the modding account linker](https://linker.ficsit.app/link). Download and install
   [the custom engine](https://github.com/satisfactorymodding/UnrealEngine/releases/latest).
3. Use the SML starter project at commit `8eebc9e659f0b2ff4392d2f8cf6e2cff60c8ea49`
   or a later revision with headers for the target game CL.
4. Install Wwise 2025.1.6.9117 and integrate Unreal integration 2025.1.6.9117.4248
   into `FactoryGame.uproject`, including the Windows SDK/platform. Generate Windows
   SoundBanks for the Wwise project.
5. Clone this repository into `<StarterProject>/Mods/GameFeatures/ResourceNodeMarker`.
   Regenerate project files, then build **Development Editor / Win64**.
6. The required `FGGameFeatureData` asset at `/ResourceNodeMarker/ResourceNodeMarker`
   is included. The helper script is available at `Scripts/create_game_feature.py` if
   you need to recreate it in another starter project.
7. Restart the editor and confirm this feature is **Active**. This mod currently adds
   no custom FGIconLibrary, FGMessage, FGUserSetting, or child input context, so it
   needs no scan rules for those types. Keep the existing SML root/config assets.
8. Compile/resave the existing Blueprint assets and package with **Alpakit Dev** for
   Windows. Use a separate test game/profile; avoid two installed copies of the mod
   under both `Mods` and `Mods/GameFeatures`.

See the [SML 3.12 migration guide](https://docs.ficsit.app/satisfactory-modding/latest/Development/UpdatingFromSml311.html)
for the engine, pointer, and Game Features changes.

## Verification status

- Development Editor / Win64 compilation: passed.
- Windows Shipping build and Alpakit package: passed.
- Game Feature asset creation and Active state: passed in the editor.
- Windows SoundBank generation: passed.
- Launch on CL 513885 and load a disposable save: not yet tested.

Runtime checks still required:

- Proximity discovery, purity colors, resource icons, and compass settings.
- Cluster merging and disabled clustering; extractor placement behavior.
- Save/reload without duplicated or lost markers, including old RNM markers.
- Non-English game language and 1.2 randomized-resource worlds.
- Leave the game running through garbage collection and repeated save loading.

Existing hard-coded icon IDs and marker ownership/reload behavior require particular
attention during playtesting. Do not publish this development branch as compatible
until the checks above pass.
