del label, probability, camera_capture, box

                # elif label == 'PERSON':
                #     print('I found a ' + str(label).lower() + '.')
                #     text = f"{label} {probability * 100:.2f}%"
                #     cv2.putText(camera_capture, text, (box[0], box[1] + 15),
                #         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                #     now = datetime.datetime.now()
                #     dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")

                #     filename = './evidence/gotcha-' + str(dt_string) + '.png'
                    
                #     cv2.imwrite(filename, camera_capture)

                #     del camera_capture

                #     recordvideo()

                #     time.sleep(30)