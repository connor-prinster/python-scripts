let main = () => {
    let str = ""
    for (let i = 0; i < 32; i++) {
        for (let j = 0; j < 24; j++) {
            str += "Dirt(" + i + ", " + j + "),"
        }
        str += "\n"
    }
    console.log(str)
}