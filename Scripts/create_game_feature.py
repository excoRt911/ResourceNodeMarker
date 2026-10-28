"""Run in the custom UE 5.6.1 editor after compiling Development Editor.

Requires Python Editor Script Plugin and Editor Scripting Utilities.
Creates only the missing ResourceNodeMarker Game Feature data asset.
"""
import unreal


def main():
    asset_path = "/ResourceNodeMarker/ResourceNodeMarker"
    feature_class = unreal.load_class(None, "/Script/FactoryGame.FGGameFeatureData")
    if feature_class is None:
        raise RuntimeError("FactoryGame.FGGameFeatureData is unavailable; use the SML 3.12 starter project.")

    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        if asset is None or asset.get_class() != feature_class:
            raise RuntimeError("The existing ResourceNodeMarker asset is not FGGameFeatureData; left unchanged.")
        unreal.log("RNM: Game Feature data already exists; left unchanged.")
        return

    factory = unreal.DataAssetFactory()
    factory.set_editor_property("data_asset_class", feature_class)
    asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        "ResourceNodeMarker", "/ResourceNodeMarker", feature_class, factory
    )
    if asset is None or not unreal.EditorAssetLibrary.save_loaded_asset(asset):
        raise RuntimeError("Could not create and save the RNM Game Feature data asset.")
    unreal.log("RNM: Created Game Feature data. Restart the editor and verify the feature is Active.")


main()
