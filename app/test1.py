

if __name__ == "__main__":

    from XCF import XCF
    from collab import Combiner
    XC = XCF.XCF()
    XC.load_image(filePath='/home/paul/dev/gimp/2x2.xcf')
    f, l = XC.get_full_image_and_layers()




    c = Combiner.Combiner(initialImage=f)
