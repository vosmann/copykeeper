function generate() {
    LOCATION=$1
    mkdir -p testbed/$LOCATION/fridge
    mkdir -p testbed/$LOCATION/freezer
}

generate local
generate remote1
generate remote2
