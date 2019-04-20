#include "opencv2/opencv.hpp"
#include "time.h"
#include <string.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include "imgProc.cpp"

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
    String image_name;
    String image_path
    for (int i = 0; i < argc; i++) {
        if (argv[i][0] == '-' && argv[i][1] == '-' && argv[i + 1] != nullptr) {
            if (strncmp(argv[i], "--i", sizeof(argv[i]) / sizeof(argv[i][0])) == 0) {
                image_name = string_split(argv[i + 1], ",");
            } else if (strncmp(argv[i], "--p", sizeof(argv[i]) / sizeof(argv[i][0])) == 0) {
                image_path = string_split(argv[i + 1], ",");
            }
        }
    }
	time_t start_time;
	time_t im_read_time, blob_detect_time;
	String srcDir, dstDir, photoName;
	int start = 9067;
	int end = 9072;
	int num;
	srcDir = "C:/Users/UHDT/Downloads/FlightTestPhotos";
	dstDir = "C:/Users/UHDT/Desktop/Test";
	for (int i = start; i <= end; i++) {
		start_time = clock();
		photoName = "/DSC_" + std::to_string(i);
		cout << "photo name: " << photoName << endl;
		imgProc(srcDir, dstDir, photoName);
		cout << "Analyzing photo " << i - start + 1 << "  of " << end - start + 1 << "\n";
		im_read_time = clock();
		printf("Took %i seconds to process images\n", (im_read_time - start_time));
	}
	waitKey(0);
	system("pause");
	return 0;
}