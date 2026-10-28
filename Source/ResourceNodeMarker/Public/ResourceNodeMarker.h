#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

#include "Resources/FGResourceNode.h"
#include "Subsystems/WorldSubsystem.h"

DECLARE_LOG_CATEGORY_EXTERN(LogResourceNodeMarker, Log, All);

class FResourceNodeMarkerModule : public IModuleInterface
{
public:
    virtual void StartupModule() override;
    virtual void ShutdownModule() override;
};
