isAutomaticMode = True
is80PercentLight = False
isDirectLight = True
isRainy = False

turnLightsOn = isAutomaticMode \
               and (not is80PercentLight \
                    or isDirectLight \
                    or isRainy)
print("TEST")
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

print("\n1. POWINNY NIE ŚWIECIĆ")
isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = False
turnLightsOn = isAutomaticMode \
               and (not is80PercentLight \
                    or isDirectLight \
                    or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

print("\n2. POWINNY ŚWIECIĆ")
isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = False
turnLightsOn = isAutomaticMode \
               and (not is80PercentLight \
                    or isDirectLight \
                    or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

print("\n3. POWINNY SIĘ ŚWIECIĆ")
isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = True
turnLightsOn = isAutomaticMode \
               and (not is80PercentLight \
                    or isDirectLight \
                    or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

print("\n4. POWINNY SIĘ ŚWIECIĆ")
isAutomaticMode = True
is80PercentLight = True
isDirectLight = True
isRainy = False
turnLightsOn = isAutomaticMode \
               and (not is80PercentLight \
                    or isDirectLight \
                    or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

print("\n5. POWINNY SIĘ ŚWIECIĆ")
isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = True
turnLightsOn = isAutomaticMode \
               and (not is80PercentLight \
                    or isDirectLight \
                    or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

print("\n6. POWINNY NIE ŚWIECIĆ")
isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True
turnLightsOn = isAutomaticMode \
               and (not is80PercentLight \
                    or isDirectLight \
                    or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

