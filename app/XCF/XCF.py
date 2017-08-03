import shutil, subprocess
import tempfile, os
import io

class XCF():

    def __init__(self):
        self.temp_dir = None

    def __del__(self):
        if self.temp_dir:
            try:
                shutil.rmtree(self.temp_dir)
            except:
                pass

    def _run_gimp(self):
        cmd = ['gimp' ,'-n', '--no-interface', '-b',
               '(python-fu-xfc-to-png RUN-NONINTERACTIVE "%s")' % self.base_xcf_path,
               '-b', '(gimp-quit 1)']
        try:
            subprocess.check_call(cmd)
        except Exception as e:
            print("exception running gimp command: %s" % str(e))


    def load_image(self, fileObj=None, filePath=None):

        self.temp_dir = tempfile.mkdtemp()
        self.base_xcf_path = os.path.join(self.temp_dir, "full.xcf")
        with open(self.base_xcf_path, "wb") as f:
            if fileObj:
                f.write(fileObj.read())
            elif filePath:
                with open(filePath, "rb") as g:
                    f.write(g.read())
            else:
                raise

    def get_full_image_and_layers(self):
        """
        get the full image as a png
        :return: a file like object in png format
        """
        full_img = io.BytesIO()
        layer_imgs = []

        self._run_gimp()
        for path in os.listdir(self.temp_dir):
            if path.split('/')[-1] == 'full.png':
                with open(os.path.join(self.temp_dir, path), "rb") as f:
                    full_img.write(f.read())
                    full_img.seek(0)
            else:
                img = io.BytesIO()
                with open(os.path.join(self.temp_dir, path), "rb") as f:
                    img.write(f.read())
                    img.seek(0)
                    layer_imgs.append(img)

        return (full_img, layer_imgs)

if __name__ == "__main__":
    xcf = XCF()
    with open("/home/paul/dev/gimp/1.xcf", "rb") as f:
        xcf.load_image(f)
    print(xcf.get_full_image_and_layers())

