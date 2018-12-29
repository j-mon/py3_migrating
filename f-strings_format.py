#Python 2 
print '{batch:3} {epoch:3} / {total_epochs:3} accuracy: {acc_mean:0.4f}±{acc_std:0.4f} time: {avg_time: 3.2f}'.format(
   batch=batch, epoch=epoch, total_epochs=total_epochs,
   acc_mean=numpy.mean(accuracies), acc_std=numpy.std(accuracies),
   avg_time=time/ len(data_batch)
)

#Python 2 (too error-prone during fast modifications, please avoid):
print '{:3} {:3} / {:3} accuracy: {:0.4f}±{:0.4f} time: {:3.2f}'.format(
      batch, epoch, total_epochs, numpy.mean(accuracies), numpy.std(accuracies),
      time / len(data_batch)
)

# Python 3.6+, f-strings formatted strings
print(f'{batch:3} {epoch:3} / {total_epochs:3} accuracy: {numpy.mean(accuracies):0.4}±{numpy.std(accuracies):0.4f} time: {time / len(data_batch):3.2f}')
