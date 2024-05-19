import subprocess
import sys
from termcolor import colored

# Function to print the rainbow banner
def print_banner():
    banner = """
  ██████  ▒█████   ███▄    █ ▓█████▄ ▓█████  ██▀███  
▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░ ████▓▒░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░ ░ ░ ▒     ░   ░ ░  ░ ░  ░    ░     ░░   ░
      ░      ░ ░           ░    ░       ░  ░   ░
    """
    version_author = "Version: 1.0.0 | Author: H3CATE"
    quote = "\"Hack the Planet\""
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for i, line in enumerate(banner.split('\n')):
        print(colored(line, colors[i % len(colors)]))
    print(colored(version_author, 'white'))
    print(colored(quote, 'white'))
    print()

# Liste des chemins de flux RTSP courants (étendue)
common_paths = [
    "/stream1",
    "/stream2",
    "/video1",
    "/video2",
    "/live.sdp",
    "/cam1/mpeg4",
    "/cam1/h264",
    "/0",
    "/1",
    "/1.avi",
    "/2.avi",
    "/3.avi",
    "/4.avi",
    "/live/ch00_0",
    "/ch1/main/av_stream",
    "/ch1/sub/av_stream",
    "/axis-media/media.amp",
    "/h264",
    "/h264.sdp",
    "/mpeg4",
    "/mpeg4.sdp",
    "/mp4",
    "/mp4.sdp",
    "/live",
    "/live.sdp",
    "/streaming/channels/1",
    "/streaming/channels/2",
    "/streaming/channels/101",
    "/streaming/channels/102",
    "/streaming/channels/201",
    "/streaming/channels/202",
    "/onvif1",
    "/onvif2",
    "/onvif/profile2/media.smp",
    "/media.smp",
    "/media/video1",
    "/media/video2",
    "/media/video3",
    "/media/video4",
    "/media/video5",
    "/media/video6",
    "/videoMain",
    "/videoSub",
    "/cam/realmonitor",
    "/live1.sdp",
    "/live2.sdp",
    "/live3.sdp",
    "/live4.sdp",
    "/live5.sdp"
]

# Fonction pour tester les URL de flux RTSP courantes avec un timeout
def test_rtsp_stream(ip_port):
    for path in common_paths:
        rtsp_url = f"rtsp://{ip_port}{path}"
        print(colored(f"Testing: {rtsp_url}", 'cyan'))
        sys.stdout.flush()  # Ensure proper flushing of output before progress bar update
        try:
            result = subprocess.run(
                ["ffmpeg", "-rtsp_transport", "tcp", "-t", "5", "-i", rtsp_url, "-f", "null", "-"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=30
            )
            stderr_output = result.stderr.decode('utf-8')
            print()  # Add a line between the ongoing test and result
            if result.returncode == 0:
                print(colored("#########################################", 'green'))
                print(colored("#                Success                #", 'green'))
                print(colored("#########################################", 'green'))
                # Ouvrir le flux avec ffplay avec des paramètres supplémentaires
                subprocess.Popen(["ffplay", "-rtsp_transport", "tcp", "-analyzeduration", "1000000000", "-probesize", "500000000", rtsp_url])
                return True
            else:
                print(colored(f"Failed: {stderr_output.splitlines()[-1]}", 'red'))
        except subprocess.TimeoutExpired:
            print(colored("Timeout", 'yellow'))
    print(colored(f"No valid stream found for {ip_port}.", 'red'))
    return False

if __name__ == "__main__":
    print_banner()
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Usage: {sys.argv[0]} <ip> [port]")
        sys.exit(1)

    ip = sys.argv[1]
    port = sys.argv[2] if len(sys.argv) == 3 else "554"
    ip_port = f"{ip}:{port}"

    # Test des flux RTSP pour l'IP fournie
    test_rtsp_stream(ip_port)

