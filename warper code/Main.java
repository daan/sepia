import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Main {

	/**
	 * @param args
	 * @throws IOException
	 */
	public static int degrees;

	public static void main(String[] args) throws IOException {
		print("java Main [degrees] [input file] [output file]");

		degrees = Integer.parseInt(args[0]);
		// TODO: read files from command line
		String file_in = args[1];
		String file_out = args[2];

		BufferedImage in = null;
		BufferedImage out = null;
		in = ImageIO.read(new File(file_in));
		out = new BufferedImage(in.getWidth(), in.getHeight(), BufferedImage.TYPE_INT_ARGB);
		warp_image(in, out);
		print("image warped");
		ImageIO.write(out, "png", new File(file_out));
		print("result written to disk");

	}

	public static void warp_image(BufferedImage in, BufferedImage out) {
		// iterate through and assign all projector angles
		for (int i = 0; i < in.getHeight(); i++)
			for (int j = 0; j < in.getWidth(); j++) {
				double temp_angle_x = (double) degrees * j / in.getWidth()
						- degrees / 2.0;
				double temp_angle_y = (double) degrees * i / in.getHeight()
						- degrees / 2.0;
				double x = angle_to_distance(temp_angle_x);
				double y = angle_to_distance(temp_angle_y);
				double sample_pos_x = (x + 1) * (in.getWidth() / 2);
				double sample_pos_y = (y + 1) * (in.getHeight() / 2);
				// print("x: " + x);
				// print("y: " + y);
				int rgb = sampled_color(sample_pos_x, sample_pos_y, in);
				out.setRGB(i, j, rgb);
			}
	}

	public static int sampled_color(double x, double y, BufferedImage img) {

		// rgb values of surrounding pixels
		int x0 = (int) x;
		int y0 = (int) y;
		int x1 = x0 + 1;
		int y1 = y0 + 1;
		// print(x0 + " " + y0);

		int x0y0, x0y1, x1y0, x1y1;
		x0y1 = x1y0 = x1y1 = x0y0 = 0xff000000;
		if (x0 < img.getWidth() && y0 < img.getHeight())
			x0y0 = img.getRGB(x0, y0);
		if (y1 < img.getHeight() && x0 < img.getWidth())
			x0y1 = img.getRGB(x0, y1);
		if (x1 < img.getWidth() && y0 < img.getHeight())
			x1y0 = img.getRGB(x1, y0);
		if (x1 < img.getWidth() && y1 < img.getHeight())
			x1y1 = img.getRGB(x1, y1);

		// weights
		double a, b;
		a = x - x0;
		b = y - y0;

		// extract pixel values [r,g,b]
		int[] v1 = get_pixel_value_array(x0y0);
		int[] v2 = get_pixel_value_array(x1y0);
		int[] v3 = get_pixel_value_array(x0y1);
		int[] v4 = get_pixel_value_array(x1y1);

		// final value
		int[] result = { 0, 0, 0 };
		int pixel = 0xff;
		for (int i = 0; i < 3; i++) {
			result[i] = (int) ((1 - a) * (1 - b) * v1[i] + a * (1 - b) * v2[i]
					+ (1 - a) * b * v3[i] + a * b * v4[i]);
			pixel <<= 8;
			pixel |= result[i];
		}

		// print("color: " + Integer.toHexString(pixel));
		return pixel;
	}

	private static int[] get_pixel_value_array(int pixel) {
		int red = (pixel >> 16) & 0xff;
		int green = (pixel >> 8) & 0xff;
		int blue = (pixel) & 0xff;
		int[] v = { red, green, blue };
		return v;
	}

	// returns a value between -1 and 1 based on a limit of +- degrees input / 2
	public static double angle_to_distance(double angle) {
		double rad = angle / 180 * Math.PI;
		double deg = ((double) degrees / 2) / 180.0 * Math.PI;
		return Math.tan(rad) / Math.tan(deg);
	}

	public static void print(String s) {
		System.out.println(s);
	}

}
