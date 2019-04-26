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
	String image_name = argv[0];
	String image_path = argv[1];
	time_t start_time;
	time_t im_read_time, blob_detect_time;

	start_time = clock();
	cout << "photo name: " << image_name << endl;
	imgProc(image_path, image_path + "/output", image_name);
	im_read_time = clock();
	printf("Took %i seconds to process images\n", (im_read_time - start_time));

	waitKey(0);
	system("pause");
	return 0;
}